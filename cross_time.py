from flask import Flask, render_template, request, jsonify
import time
import threading
import datetime
import os
import platform
import subprocess
import sys

app = Flask(__name__)

class TimerManager:
    def __init__(self):
        self.active_timers = {}
        self.timer_status = {}
        self.timer_id_counter = 0
        self.should_stop = {}  # Controle de parada
        
    def beep(self):
        """Emitir sinal sonoro multiplataforma"""
        try:
            if platform.system() == "Windows":
                import winsound
                winsound.Beep(1000, 500)
            elif platform.system() == "Darwin":  # macOS
                os.system('afplay 32642695_vK227VA.mp3')
            else:  # Linux
                # Tenta vários métodos para Linux
                try:
                    # Método 1: Usando speaker-test (geralmente disponível)
                    os.system('timeout 0.5s speaker-test -t sine -f 1000 > /dev/null 2>&1')
                except:
                    try:
                        # Método 2: Usando beep (se instalado)
                        os.system('beep -f 1000 -l 500 > /dev/null 2>&1')
                    except:
                        # Método 3: Usando printf com bell character
                        print('\a', end='', flush=True)
        except Exception as e:
            print(f"Erro ao emitir som: {e}")
    
    def show_popup(self, message):
        """Mostrar notificação - alternativa ao tkinter"""
        try:
            # Tenta usar notify-send no Linux
            if platform.system() == "Linux":
                os.system(f'notify-send "Cronômetro" "{message}"')
            elif platform.system() == "Darwin":  # macOS
                os.system(f'osascript -e \'display notification "{message}" with title "Cronômetro"\'')
            elif platform.system() == "Windows":
                # Para Windows, tenta importar winsound apenas se necessário
                try:
                    import winsound
                    winsound.MessageBeep()
                except:
                    pass
            
            # Sempre imprime no console como fallback
            print(f"🔔 NOTIFICAÇÃO: {message}")
            
        except Exception as e:
            print(f"Erro ao mostrar notificação: {e}")
            print(f"⏰ TIMER: {message}")
    
    def start_timer(self, total_time, interval, rounds=None, rest_time=None):
        """Iniciar cronômetro com contagem progressiva"""
        timer_id = self.timer_id_counter
        self.timer_id_counter += 1
        self.should_stop[timer_id] = False
        
        def timer_thread():
            # Calcular tempo por round
            round_duration = (total_time * 60) / rounds if rounds and rounds > 0 else total_time * 60
            total_rounds = rounds if rounds and rounds > 0 else 1
            
            print(f"🎯 Timer {timer_id} iniciado: {total_time}min, {total_rounds} rounds de {round_duration}seg cada, Descanso: {rest_time}seg")
            
            # Inicializar status
            self.timer_status[timer_id] = {
                'total_time': total_time * 60,
                'round_duration': round_duration,
                'total_rounds': total_rounds,
                'rest_time': rest_time if rest_time else 0,
                'interval': interval,
                'current_round': 1,
                'current_phase': 'countdown',  # countdown, work, rest
                'round_elapsed': 0,
                'total_elapsed': 0,
                'is_running': True,
                'countdown_seconds': 10
            }
            
            # CONTAGEM REGRESSIVA INICIAL (10 segundos) - apenas para o primeiro round
            print(f"⏰ Contagem regressiva inicial para Round 1")
            for i in range(10, 0, -1):
                if self.should_stop[timer_id]:
                    return
                
                self.timer_status[timer_id]['countdown_seconds'] = i
                time.sleep(1)
            
            if self.should_stop[timer_id]:
                return
            
            self.beep()
            self.show_popup("🎯 Round 1 iniciado!")
            print("🎯 Round 1 iniciado")
            
            # Iniciar o primeiro round
            self.timer_status[timer_id].update({
                'current_phase': 'work',
                'countdown_seconds': 0,
                'round_start_time': time.time()
            })
            
            round_start_time = time.time()
            last_interval_beep = 0
            current_round = 1
            
            # LOOP PRINCIPAL DOS ROUNDS
            while current_round <= total_rounds and not self.should_stop[timer_id]:
                # FASE DE TRABALHO (contagem progressiva)
                if self.timer_status[timer_id]['current_phase'] == 'work':
                    round_elapsed = time.time() - round_start_time
                    
                    # Atualizar status
                    self.timer_status[timer_id].update({
                        'round_elapsed': round_elapsed,
                        'total_elapsed': (current_round - 1) * round_duration + round_elapsed,
                        'current_round': current_round
                    })
                    
                    # Verificar se o round terminou
                    if round_elapsed >= round_duration:
                        # Round finalizado
                        if current_round < total_rounds and rest_time and rest_time > 0:
                            # Ir para descanso
                            self.timer_status[timer_id]['current_phase'] = 'rest'
                            self.show_popup(f"🔄 Round {current_round} finalizado! Descanso de {rest_time} segundos.")
                            print(f"🔄 Round {current_round} finalizado - Iniciando descanso")
                            
                            # CONTAGEM REGRESSIVA DO DESCANSO
                            rest_start = time.time()
                            rest_elapsed = 0
                            
                            while rest_elapsed < rest_time and not self.should_stop[timer_id]:
                                rest_elapsed = time.time() - rest_start
                                remaining_rest = rest_time - int(rest_elapsed)
                                self.timer_status[timer_id]['countdown_seconds'] = remaining_rest
                                time.sleep(0.1)
                            
                            if self.should_stop[timer_id]:
                                break
                            
                            # FIM DO DESCANSO - INICIAR PRÓXIMO ROUND IMEDIATAMENTE
                            current_round += 1
                            self.beep()
                            self.show_popup(f"🎯 Round {current_round} iniciado!")
                            print(f"🎯 Round {current_round} iniciado")
                            
                            self.timer_status[timer_id].update({
                                'current_phase': 'work',
                                'countdown_seconds': 0,
                                'current_round': current_round
                            })
                            round_start_time = time.time()
                            
                        else:
                            # Sem descanso ou último round
                            current_round += 1
                            if current_round <= total_rounds:
                                # Próximo round sem descanso
                                self.timer_status[timer_id].update({
                                    'current_phase': 'work',
                                    'countdown_seconds': 0,
                                    'current_round': current_round
                                })
                                round_start_time = time.time()
                                self.beep()
                                self.show_popup(f"🎯 Round {current_round} iniciado!")
                                print(f"🎯 Round {current_round} iniciado")
                    
                    # Sinal sonoro a cada intervalo
                    if (interval > 0 and 
                        round_elapsed - last_interval_beep >= interval * 60 and
                        not self.should_stop[timer_id]):
                        
                        self.beep()
                        last_interval_beep = round_elapsed
                        print(f"🔊 Sinal sonoro no Round {current_round} - {int(round_elapsed//60)}min decorridos")
                
                time.sleep(0.1)  # Loop responsivo
            
            # Timer finalizado ou parado
            if not self.should_stop[timer_id]:
                self.beep()
                self.show_popup("🎉 Todos os rounds finalizados!")
                print(f"✅ Timer {timer_id} finalizado!")
            else:
                print(f"⏹️ Timer {timer_id} parado pelo usuário")
            
            # Finalizar status
            self.timer_status[timer_id]['is_running'] = False
            
            # Limpar recursos
            if timer_id in self.active_timers:
                del self.active_timers[timer_id]
            if timer_id in self.should_stop:
                del self.should_stop[timer_id]
            if timer_id in self.timer_status:
                # Manter o status por um tempo para o frontend detectar a parada
                time.sleep(2)
                del self.timer_status[timer_id]
        
        thread = threading.Thread(target=timer_thread)
        thread.daemon = True
        self.active_timers[timer_id] = thread
        thread.start()
        
        return timer_id

    def stop_timer(self, timer_id):
        """Parar timer específico"""
        print(f"🛑 Tentando parar timer {timer_id}")
        if timer_id in self.active_timers:
            self.should_stop[timer_id] = True
            if timer_id in self.timer_status:
                self.timer_status[timer_id]['is_running'] = False
            print(f"✅ Timer {timer_id} marcado para parada")
            return True
        print(f"❌ Timer {timer_id} não encontrado para parada")
        return False

    def is_timer_running(self, timer_id):
        """Verificar se o timer está rodando"""
        return (timer_id in self.active_timers and 
                not self.should_stop.get(timer_id, False) and
                self.timer_status.get(timer_id, {}).get('is_running', False))

timer_manager = TimerManager()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start_timer', methods=['POST'])
def start_timer():
    data = request.json
    
    total_time = data.get('total_time', 0)
    interval = data.get('interval', 0)
    rounds = data.get('rounds', 0)
    rest_time = data.get('rest_time', 0)
    
    if total_time <= 0:
        return jsonify({'error': 'Tempo total deve ser maior que 0'}), 400
    
    if rounds and rounds > 0 and total_time * 60 / rounds <= 0:
        return jsonify({'error': 'Tempo por round deve ser maior que 0'}), 400
    
    timer_id = timer_manager.start_timer(total_time, interval, rounds, rest_time)
    
    return jsonify({
        'message': 'Timer iniciado',
        'timer_id': timer_id,
        'start_time': datetime.datetime.now().strftime('%H:%M:%S')
    })

@app.route('/current_time')
def current_time():
    return jsonify({
        'current_time': datetime.datetime.now().strftime('%H:%M:%S'),
        'current_date': datetime.datetime.now().strftime('%d/%m/%Y')
    })

@app.route('/timer_status/<int:timer_id>')
def timer_status(timer_id):
    if timer_id in timer_manager.timer_status:
        status = timer_manager.timer_status[timer_id]
        return jsonify({
            'is_running': status['is_running'] and timer_manager.is_timer_running(timer_id),
            'is_countdown': status['current_phase'] == 'countdown',
            'countdown_seconds': status.get('countdown_seconds', 0),
            'current_phase': status['current_phase'],
            'round_elapsed': int(status['round_elapsed']),
            'total_elapsed': int(status['total_elapsed']),
            'total_time': int(status['total_time']),
            'current_round': status['current_round'],
            'total_rounds': status['total_rounds'],
            'round_duration': int(status['round_duration']),
            'rest_time': status.get('rest_time', 0),
            'progress': (status['total_elapsed'] / status['total_time']) * 100 if status['total_time'] > 0 else 0,
            'round_progress': (status['round_elapsed'] / status['round_duration']) * 100 if status['round_duration'] > 0 else 0
        })
    return jsonify({'error': 'Timer não encontrado'}), 404

@app.route('/stop_timer/<int:timer_id>')
def stop_timer(timer_id):
    if timer_manager.stop_timer(timer_id):
        return jsonify({'message': 'Timer parado com sucesso', 'stopped': True})
    return jsonify({'error': 'Timer não encontrado'}), 404

@app.route('/active_timers')
def active_timers():
    active_timers_list = [timer_id for timer_id in timer_manager.active_timers 
                         if not timer_manager.should_stop.get(timer_id, False)]
    return jsonify({
        'active_count': len(active_timers_list),
        'timers': active_timers_list
    })

if __name__ == '__main__':
    print("🚀 Cronômetro Inteligente iniciando...")
    print("📧 Acesse: http://localhost:5000")
    print("💡 Dica: Use Ctrl+C para parar o servidor")
    app.run(debug=True, host='0.0.0.0', port=5000)
