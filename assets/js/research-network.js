// Interactive Research Network Graph
class ResearchNetwork {
    constructor(containerId, data) {
        this.container = document.getElementById(containerId);
        if (!this.container) return;
        
        this.data = data;
        this.width = this.container.offsetWidth;
        this.height = 600;
        this.selectedNode = null;
        
        this.init();
    }
    
    init() {
        // Create canvas
        this.canvas = document.createElement('canvas');
        this.canvas.width = this.width;
        this.canvas.height = this.height;
        this.canvas.style.width = '100%';
        this.canvas.style.height = '600px';
        this.container.appendChild(this.canvas);
        
        this.ctx = this.canvas.getContext('2d');
        
        // Create info panel
        this.infoPanel = document.createElement('div');
        this.infoPanel.className = 'research-info-panel';
        this.infoPanel.style.cssText = `
            position: absolute;
            top: 20px;
            right: 20px;
            width: 300px;
            background: var(--global-card-bg-color);
            border: 1px solid var(--global-divider-color);
            border-radius: 10px;
            padding: 20px;
            opacity: 0;
            transform: translateX(20px);
            transition: all 0.3s ease;
            backdrop-filter: blur(10px);
            box-shadow: 0 10px 30px rgba(0,0,0,0.1);
        `;
        this.container.style.position = 'relative';
        this.container.appendChild(this.infoPanel);
        
        // Initialize nodes with positions
        this.initializeNodes();
        
        // Event listeners
        this.canvas.addEventListener('mousemove', (e) => this.handleMouseMove(e));
        this.canvas.addEventListener('click', (e) => this.handleClick(e));
        window.addEventListener('resize', () => this.handleResize());
        
        // Start animation
        this.animate();
    }
    
    initializeNodes() {
        const centerX = this.width / 2;
        const centerY = this.height / 2;
        
        // Central node
        this.nodes = [{
            id: 'center',
            label: 'Research Interests',
            x: centerX,
            y: centerY,
            vx: 0,
            vy: 0,
            radius: 40,
            color: 'var(--global-theme-color)',
            fixed: true,
            description: 'Click on any node to explore my research interests',
            links: []
        }];
        
        // Research area nodes
        const areas = this.data.length;
        const angleStep = (Math.PI * 2) / areas;
        const orbitRadius = Math.min(this.width, this.height) * 0.3;
        
        this.data.forEach((area, index) => {
            const angle = index * angleStep - Math.PI / 2;
            const x = centerX + Math.cos(angle) * orbitRadius;
            const y = centerY + Math.sin(angle) * orbitRadius;
            
            this.nodes.push({
                id: area.id,
                label: area.label,
                x: x,
                y: y,
                vx: 0,
                vy: 0,
                radius: 30,
                color: area.color || 'var(--global-hover-color)',
                description: area.description,
                links: area.links || [],
                papers: area.papers || [],
                targetX: x,
                targetY: y,
                expanded: false
            });
        });
        
        // Create connections
        this.connections = [];
        for (let i = 1; i < this.nodes.length; i++) {
            this.connections.push({
                source: 0,
                target: i
            });
        }
    }
    
    handleMouseMove(e) {
        const rect = this.canvas.getBoundingClientRect();
        this.mouseX = (e.clientX - rect.left) * (this.canvas.width / rect.width);
        this.mouseY = (e.clientY - rect.top) * (this.canvas.height / rect.height);
        
        // Check hover
        this.hoveredNode = null;
        this.nodes.forEach(node => {
            const dx = this.mouseX - node.x;
            const dy = this.mouseY - node.y;
            const distance = Math.sqrt(dx * dx + dy * dy);
            
            if (distance < node.radius) {
                this.hoveredNode = node;
                this.canvas.style.cursor = 'pointer';
            }
        });
        
        if (!this.hoveredNode) {
            this.canvas.style.cursor = 'default';
        }
    }
    
    handleClick(e) {
        if (this.hoveredNode && this.hoveredNode.id !== 'center') {
            this.selectNode(this.hoveredNode);
        }
    }
    
    selectNode(node) {
        this.selectedNode = node;
        
        // Show info panel
        this.infoPanel.style.opacity = '1';
        this.infoPanel.style.transform = 'translateX(0)';
        
        // Update info panel content
        let content = `
            <h3 style="color: var(--global-theme-color); margin-bottom: 15px;">${node.label}</h3>
            <p style="color: var(--global-text-color); margin-bottom: 15px;">${node.description}</p>
        `;
        
        if (node.papers && node.papers.length > 0) {
            content += '<h4 style="color: var(--global-hover-color); margin-bottom: 10px;">Related Papers:</h4><ul style="list-style: none; padding: 0;">';
            node.papers.forEach(paper => {
                content += `<li style="margin-bottom: 8px;">
                    <a href="${paper.url}" target="_blank" style="color: var(--global-accent-color);">
                        ${paper.title}
                    </a>
                </li>`;
            });
            content += '</ul>';
        }
        
        if (node.links && node.links.length > 0) {
            content += '<h4 style="color: var(--global-hover-color); margin-top: 15px; margin-bottom: 10px;">Links:</h4><ul style="list-style: none; padding: 0;">';
            node.links.forEach(link => {
                content += `<li style="margin-bottom: 8px;">
                    <a href="${link.url}" target="_blank" style="color: var(--global-text-color);">
                        ${link.label}
                    </a>
                </li>`;
            });
            content += '</ul>';
        }
        
        this.infoPanel.innerHTML = content;
        
        // Expand node connections
        node.expanded = !node.expanded;
    }
    
    handleResize() {
        this.width = this.container.offsetWidth;
        this.canvas.width = this.width;
        this.initializeNodes();
    }
    
    update() {
        // Physics simulation
        this.nodes.forEach((node, i) => {
            if (node.fixed) return;
            
            // Spring force to target position
            const dx = node.targetX - node.x;
            const dy = node.targetY - node.y;
            node.vx += dx * 0.05;
            node.vy += dy * 0.05;
            
            // Damping
            node.vx *= 0.9;
            node.vy *= 0.9;
            
            // Update position
            node.x += node.vx;
            node.y += node.vy;
            
            // Mouse repulsion
            if (this.mouseX && this.mouseY) {
                const mdx = node.x - this.mouseX;
                const mdy = node.y - this.mouseY;
                const mdist = Math.sqrt(mdx * mdx + mdy * mdy);
                
                if (mdist < 100 && mdist > 0) {
                    const force = (1 - mdist / 100) * 2;
                    node.vx += (mdx / mdist) * force;
                    node.vy += (mdy / mdist) * force;
                }
            }
        });
    }
    
    draw() {
        // Clear canvas
        this.ctx.clearRect(0, 0, this.width, this.height);
        
        // Draw connections
        this.ctx.strokeStyle = 'var(--global-divider-color)';
        this.ctx.lineWidth = 2;
        
        this.connections.forEach(conn => {
            const source = this.nodes[conn.source];
            const target = this.nodes[conn.target];
            
            this.ctx.beginPath();
            this.ctx.moveTo(source.x, source.y);
            this.ctx.lineTo(target.x, target.y);
            this.ctx.stroke();
        });
        
        // Draw nodes
        this.nodes.forEach(node => {
            const isHovered = node === this.hoveredNode;
            const isSelected = node === this.selectedNode;
            const scale = isHovered ? 1.2 : (isSelected ? 1.1 : 1);
            const radius = node.radius * scale;
            
            // Node glow
            if (isHovered || isSelected) {
                const gradient = this.ctx.createRadialGradient(
                    node.x, node.y, 0,
                    node.x, node.y, radius * 2
                );
                gradient.addColorStop(0, node.color + '40');
                gradient.addColorStop(1, 'transparent');
                
                this.ctx.beginPath();
                this.ctx.arc(node.x, node.y, radius * 2, 0, Math.PI * 2);
                this.ctx.fillStyle = gradient;
                this.ctx.fill();
            }
            
            // Node circle
            this.ctx.beginPath();
            this.ctx.arc(node.x, node.y, radius, 0, Math.PI * 2);
            this.ctx.fillStyle = node.color;
            this.ctx.fill();
            
            // Node border
            this.ctx.strokeStyle = isHovered || isSelected ? '#fff' : 'var(--global-divider-color)';
            this.ctx.lineWidth = 2;
            this.ctx.stroke();
            
            // Node label
            this.ctx.fillStyle = 'var(--global-text-color)';
            this.ctx.font = `${isHovered ? '14px' : '12px'} Inter, sans-serif`;
            this.ctx.textAlign = 'center';
            this.ctx.textBaseline = 'middle';
            
            // Word wrap for long labels
            const words = node.label.split(' ');
            const lineHeight = 16;
            let line = '';
            let y = node.y;
            
            if (words.length > 2 && !isHovered) {
                // Show abbreviated version when not hovered
                this.ctx.fillText(words[0] + '...', node.x, y);
            } else {
                // Show full text
                for (let n = 0; n < words.length; n++) {
                    const testLine = line + words[n] + ' ';
                    const metrics = this.ctx.measureText(testLine);
                    const testWidth = metrics.width;
                    
                    if (testWidth > radius * 2 && n > 0) {
                        this.ctx.fillText(line, node.x, y);
                        line = words[n] + ' ';
                        y += lineHeight;
                    } else {
                        line = testLine;
                    }
                }
                this.ctx.fillText(line, node.x, y);
            }
        });
    }
    
    animate() {
        this.update();
        this.draw();
        requestAnimationFrame(() => this.animate());
    }
}

// Research data
const researchData = [
    {
        id: 'llms',
        label: 'LLMs/VLMs',
        color: '#6B46C1',
        description: 'Large Language Models and Vision-Language Models research, including mechanistic interpretability, compositionality, and practical applications.',
        papers: [
            { title: 'Compositionality in LLMs', url: 'https://arxiv.org/pdf/2410.01444' },
            { title: 'Causal Graph Discovery with LLMs', url: 'https://arxiv.org/pdf/2402.01207' }
        ],
        links: [
            { label: 'Anthropic Fellowship', url: 'https://www.anthropic.com/' },
            { label: 'Occam AI Internship', url: 'https://www.occam.ai/' }
        ]
    },
    {
        id: 'neuroai',
        label: 'NeuroAI',
        color: '#3B82F6',
        description: 'Neuroscience and cognitive science inspired AI, focusing on biologically plausible learning mechanisms and input-driven learning.',
        papers: [
            { title: 'Bias-only Learning', url: 'https://arxiv.org/pdf/2407.00957' }
        ]
    },
    {
        id: 'modularity',
        label: 'Modularity',
        color: '#06B6D4',
        description: 'Research on compositionality, discrete representations, and modular architectures in AI systems.',
        papers: [
            { title: 'Complexity-based Theory of Compositionality', url: 'https://arxiv.org/pdf/2410.14817' },
            { title: 'Discovering Discrete Subgoals for RL', url: 'https://arxiv.org/pdf/2210.05845' }
        ]
    },
    {
        id: 'causality',
        label: 'Model-based AI',
        color: '#EC4899',
        description: 'Causality, model-based reinforcement learning, and structured reasoning in AI systems.',
        papers: [
            { title: 'Causal Imputation', url: 'https://arxiv.org/pdf/2410.20647' },
            { title: 'Temporally Extended Tree-Search Planning', url: 'https://arxiv.org/pdf/2310.09997' }
        ]
    },
    {
        id: 'ai4good',
        label: 'AI for Good',
        color: '#F97316',
        description: 'Applications of AI for social good including healthcare, climate change, autonomous driving, and drug discovery.',
        papers: [
            { title: 'RL for Mechanical Ventilation', url: 'https://ojs.aaai.org/index.php/AAAI/article/view/26862' },
            { title: 'RL for HVAC Control', url: 'https://arxiv.org/pdf/2308.05711' }
        ],
        links: [
            { label: 'Waabi Internship', url: 'https://waabi.ai/' }
        ]
    }
];

// Initialize when DOM is ready
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', () => {
        const container = document.getElementById('research-network');
        if (container) {
            window.researchNetwork = new ResearchNetwork('research-network', researchData);
        }
    });
} else {
    const container = document.getElementById('research-network');
    if (container) {
        window.researchNetwork = new ResearchNetwork('research-network', researchData);
    }
}