// Easter Eggs and Interactive ML Demo
(function() {
    'use strict';
    
    // Konami Code Easter Egg
    const konamiCode = ['ArrowUp', 'ArrowUp', 'ArrowDown', 'ArrowDown', 'ArrowLeft', 'ArrowRight', 'ArrowLeft', 'ArrowRight', 'b', 'a'];
    let konamiIndex = 0;
    
    document.addEventListener('keydown', (e) => {
        if (e.key === konamiCode[konamiIndex]) {
            konamiIndex++;
            if (konamiIndex === konamiCode.length) {
                activateMatrixMode();
                konamiIndex = 0;
            }
        } else {
            konamiIndex = 0;
        }
    });
    
    // Matrix Mode
    function activateMatrixMode() {
        const canvas = document.createElement('canvas');
        canvas.id = 'matrix-rain';
        canvas.style.cssText = `
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            z-index: 9998;
            pointer-events: none;
        `;
        document.body.appendChild(canvas);
        
        const ctx = canvas.getContext('2d');
        canvas.width = window.innerWidth;
        canvas.height = window.innerHeight;
        
        const chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789@#$%^&*()_+-=[]{}|;:,.<>?~';
        const fontSize = 14;
        const columns = canvas.width / fontSize;
        const drops = Array(Math.floor(columns)).fill(1);
        
        ctx.font = fontSize + 'px monospace';
        
        function draw() {
            ctx.fillStyle = 'rgba(0, 0, 0, 0.05)';
            ctx.fillRect(0, 0, canvas.width, canvas.height);
            
            ctx.fillStyle = '#0F0';
            for (let i = 0; i < drops.length; i++) {
                const text = chars[Math.floor(Math.random() * chars.length)];
                ctx.fillText(text, i * fontSize, drops[i] * fontSize);
                
                if (drops[i] * fontSize > canvas.height && Math.random() > 0.975) {
                    drops[i] = 0;
                }
                drops[i]++;
            }
        }
        
        const matrixInterval = setInterval(draw, 35);
        
        // Remove after 10 seconds
        setTimeout(() => {
            clearInterval(matrixInterval);
            canvas.remove();
            showNotification('Matrix mode deactivated!');
        }, 10000);
        
        showNotification('Matrix mode activated! 🎬');
    }
    
    // Neural Network Visualizer (Press 'n' key)
    let neuralVisualizerActive = false;
    document.addEventListener('keydown', (e) => {
        if (e.key === 'n' && !e.ctrlKey && !e.metaKey && !e.altKey) {
            toggleNeuralVisualizer();
        }
    });
    
    function toggleNeuralVisualizer() {
        if (neuralVisualizerActive) {
            const visualizer = document.getElementById('neural-visualizer');
            if (visualizer) visualizer.remove();
            neuralVisualizerActive = false;
            return;
        }
        
        neuralVisualizerActive = true;
        const container = document.createElement('div');
        container.id = 'neural-visualizer';
        container.innerHTML = `
            <div style="
                position: fixed;
                bottom: 20px;
                right: 20px;
                width: 300px;
                height: 200px;
                background: rgba(20, 20, 31, 0.95);
                border: 2px solid var(--global-theme-color);
                border-radius: 10px;
                padding: 15px;
                z-index: 9997;
                backdrop-filter: blur(10px);
                box-shadow: 0 10px 30px rgba(0,0,0,0.5);
            ">
                <h4 style="color: var(--global-theme-color); margin: 0 0 10px 0; font-size: 14px;">Mini Neural Network</h4>
                <canvas id="mini-nn-canvas" width="270" height="140"></canvas>
                <div style="position: absolute; top: 10px; right: 10px; cursor: pointer; color: #fff;" onclick="this.parentElement.parentElement.remove(); neuralVisualizerActive = false;">✕</div>
            </div>
        `;
        document.body.appendChild(container);
        
        // Draw mini neural network
        const canvas = document.getElementById('mini-nn-canvas');
        const ctx = canvas.getContext('2d');
        
        const layers = [3, 4, 2];
        const neurons = [];
        
        // Calculate neuron positions
        layers.forEach((count, layerIndex) => {
            const layerNeurons = [];
            const x = 50 + layerIndex * 85;
            const layerHeight = count * 30;
            const startY = (140 - layerHeight) / 2 + 15;
            
            for (let i = 0; i < count; i++) {
                layerNeurons.push({
                    x: x,
                    y: startY + i * 30,
                    activation: Math.random()
                });
            }
            neurons.push(layerNeurons);
        });
        
        function drawMiniNN() {
            ctx.clearRect(0, 0, 270, 140);
            
            // Draw connections
            for (let i = 0; i < neurons.length - 1; i++) {
                for (let j = 0; j < neurons[i].length; j++) {
                    for (let k = 0; k < neurons[i + 1].length; k++) {
                        const weight = Math.random();
                        ctx.strokeStyle = `rgba(107, 70, 193, ${weight})`;
                        ctx.lineWidth = weight * 2;
                        ctx.beginPath();
                        ctx.moveTo(neurons[i][j].x, neurons[i][j].y);
                        ctx.lineTo(neurons[i + 1][k].x, neurons[i + 1][k].y);
                        ctx.stroke();
                    }
                }
            }
            
            // Draw neurons
            neurons.forEach((layer, layerIndex) => {
                layer.forEach(neuron => {
                    neuron.activation = Math.max(0, Math.min(1, neuron.activation + (Math.random() - 0.5) * 0.1));
                    
                    const gradient = ctx.createRadialGradient(neuron.x, neuron.y, 0, neuron.x, neuron.y, 8);
                    gradient.addColorStop(0, `rgba(6, 182, 212, ${neuron.activation})`);
                    gradient.addColorStop(1, 'transparent');
                    
                    ctx.beginPath();
                    ctx.arc(neuron.x, neuron.y, 8, 0, Math.PI * 2);
                    ctx.fillStyle = gradient;
                    ctx.fill();
                    
                    ctx.beginPath();
                    ctx.arc(neuron.x, neuron.y, 6, 0, Math.PI * 2);
                    ctx.fillStyle = `rgba(255, 255, 255, ${0.5 + neuron.activation * 0.5})`;
                    ctx.fill();
                });
            });
            
            if (neuralVisualizerActive) {
                requestAnimationFrame(drawMiniNN);
            }
        }
        
        drawMiniNN();
        showNotification('Press "n" to toggle neural network visualizer');
    }
    
    // Click counter Easter egg
    let clickCount = 0;
    let clickTimer;
    
    document.addEventListener('click', (e) => {
        if (e.target.closest('.post-title')) {
            clickCount++;
            clearTimeout(clickTimer);
            
            if (clickCount === 7) {
                launchFireworks();
                clickCount = 0;
            }
            
            clickTimer = setTimeout(() => {
                clickCount = 0;
            }, 2000);
        }
    });
    
    // Fireworks animation
    function launchFireworks() {
        const canvas = document.createElement('canvas');
        canvas.id = 'fireworks';
        canvas.style.cssText = `
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            pointer-events: none;
            z-index: 9999;
        `;
        document.body.appendChild(canvas);
        
        const ctx = canvas.getContext('2d');
        canvas.width = window.innerWidth;
        canvas.height = window.innerHeight;
        
        const particles = [];
        const colors = ['#6B46C1', '#3B82F6', '#06B6D4', '#EC4899', '#F97316'];
        
        class Particle {
            constructor(x, y, color) {
                this.x = x;
                this.y = y;
                this.vx = (Math.random() - 0.5) * 8;
                this.vy = (Math.random() - 0.5) * 8;
                this.color = color;
                this.life = 1;
                this.decay = Math.random() * 0.02 + 0.01;
            }
            
            update() {
                this.x += this.vx;
                this.y += this.vy;
                this.vy += 0.1;
                this.life -= this.decay;
            }
            
            draw(ctx) {
                ctx.save();
                ctx.globalAlpha = this.life;
                ctx.fillStyle = this.color;
                ctx.shadowBlur = 10;
                ctx.shadowColor = this.color;
                ctx.beginPath();
                ctx.arc(this.x, this.y, 3, 0, Math.PI * 2);
                ctx.fill();
                ctx.restore();
            }
        }
        
        function createFirework(x, y) {
            const color = colors[Math.floor(Math.random() * colors.length)];
            for (let i = 0; i < 50; i++) {
                particles.push(new Particle(x, y, color));
            }
        }
        
        // Create multiple fireworks
        for (let i = 0; i < 5; i++) {
            setTimeout(() => {
                createFirework(
                    Math.random() * canvas.width,
                    Math.random() * canvas.height * 0.5
                );
            }, i * 200);
        }
        
        function animate() {
            ctx.fillStyle = 'rgba(0, 0, 0, 0.1)';
            ctx.fillRect(0, 0, canvas.width, canvas.height);
            
            particles.forEach((particle, index) => {
                particle.update();
                particle.draw(ctx);
                
                if (particle.life <= 0) {
                    particles.splice(index, 1);
                }
            });
            
            if (particles.length > 0) {
                requestAnimationFrame(animate);
            } else {
                canvas.remove();
            }
        }
        
        animate();
        showNotification('🎆 Achievement unlocked: Secret clicker!');
    }
    
    // Notification system
    function showNotification(message) {
        const notification = document.createElement('div');
        notification.style.cssText = `
            position: fixed;
            top: 20px;
            left: 50%;
            transform: translateX(-50%);
            background: var(--global-card-bg-color);
            color: var(--global-text-color);
            padding: 15px 25px;
            border-radius: 10px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.3);
            z-index: 10000;
            animation: slideDown 0.3s ease;
            border: 1px solid var(--global-theme-color);
        `;
        notification.textContent = message;
        document.body.appendChild(notification);
        
        setTimeout(() => {
            notification.style.animation = 'slideUp 0.3s ease';
            setTimeout(() => notification.remove(), 300);
        }, 3000);
    }
    
    // Add notification animations
    const style = document.createElement('style');
    style.textContent = `
        @keyframes slideDown {
            from {
                transform: translate(-50%, -100%);
                opacity: 0;
            }
            to {
                transform: translate(-50%, 0);
                opacity: 1;
            }
        }
        
        @keyframes slideUp {
            from {
                transform: translate(-50%, 0);
                opacity: 1;
            }
            to {
                transform: translate(-50%, -100%);
                opacity: 0;
            }
        }
    `;
    document.head.appendChild(style);
    
    // Console Easter egg
    console.log('%c🧠 Welcome to the Neural Network Theme! 🧠', 'font-size: 20px; color: #6B46C1; font-weight: bold;');
    console.log('%cTry these easter eggs:', 'font-size: 14px; color: #06B6D4;');
    console.log('%c- Konami Code: ↑↑↓↓←→←→BA', 'font-size: 12px; color: #3B82F6;');
    console.log('%c- Press "n" for neural network visualizer', 'font-size: 12px; color: #3B82F6;');
    console.log('%c- Click the title 7 times quickly', 'font-size: 12px; color: #3B82F6;');
    console.log('%c- More secrets hidden... 🔍', 'font-size: 12px; color: #EC4899;');
    
})();