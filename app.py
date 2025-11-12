from flask import Flask, render_template, request, redirect, url_for, flash
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'

# Complete project data with all your projects
projects = [
    {
        "id": 1,
        "title": "Smart Greenhouse System", 
        "description": "Automated IoT greenhouse with environmental control and crop optimization.",
        "full_description": "A complete IoT-based greenhouse automation system that monitors temperature, humidity, soil moisture and controls irrigation, ventilation, and lighting automatically. Features remote monitoring via web dashboard and mobile app with ESP32-CAM integration.",
        "technologies": ["ESP32", "IoT", "C++", "Python", "MQTT", "JSON API", "ESP32-CAM"],
        "image": "greenhouse.jpg",
        "github": "#",
        "demo": "#",
        "category": "IoT & Automation",
        "status": "Active",
        "icon": "seedling"
    },
    {
        "id": 2,
        "title": "Smart Energy Meter with Theft Detection", 
        "description": "Electrical engineering project measuring power consumption and detecting reverse current.",
        "full_description": "Advanced energy monitoring system that detects power theft, provides real-time consumption data using ACS712 and ZMPT101B sensors, and offers predictive analytics for energy savings.",
        "technologies": ["ESP32", "Arduino", "C++", "ACS712", "ZMPT101B", "Electrical Engineering"],
        "image": "energy-meter.jpg",
        "github": "#",
        "demo": "#",
        "category": "Electrical Engineering",
        "status": "Prototype",
        "icon": "bolt"
    },
    {
        "id": 3,
        "title": "Self-Balancing Robot", 
        "description": "2-wheel robot using MPU6050 and PID control for autonomous balancing.",
        "full_description": "Autonomous self-balancing robot that uses MPU6050 gyroscope/accelerometer and PID control algorithms. Capable of navigating uneven terrain and maintaining balance in dynamic conditions with DC gear motors and L298N driver.",
        "technologies": ["PID Control", "MPU6050", "Arduino", "C++", "L298N", "Robotics"],
        "image": "robot.jpg",
        "github": "#",
        "demo": "#",
        "category": "Robotics",
        "status": "Prototype",
        "icon": "robot"
    },
    {
        "id": 4,
        "title": "BroodinnoX Smart Brooding System", 
        "description": "IoT-based poultry brooding system with MQTT dashboard integration.",
        "full_description": "Automated chicken brooding system with temperature control using multiple DHT22 sensors, heating control via relays, and MQTT integration for remote monitoring and control.",
        "technologies": ["ESP32", "DHT22", "MQTT", "C++", "RTC", "Agriculture IoT"],
        "image": "brooding.jpg",
        "github": "#",
        "demo": "#",
        "category": "IoT & Agriculture",
        "status": "Active",
        "icon": "temperature-high"
    },
    {
        "id": 5,
        "title": "Autonomous Waiter Robot", 
        "description": "Service robot with ROS navigation and voice recognition for food delivery.",
        "full_description": "Final-year mechatronics project combining ROS, computer vision, and sensor integration for autonomous navigation, voice recognition order capture, and obstacle avoidance in restaurant environments.",
        "technologies": ["ROS", "Python", "OpenCV", "Raspberry Pi", "Ultrasonic", "Mechatronics"],
        "image": "waiter-robot.jpg",
        "github": "#",
        "demo": "#",
        "category": "Mechatronics",
        "status": "Prototype",
        "icon": "utensils"
    },
    {
        "id": 6,
        "title": "Speed Sign Detection System", 
        "description": "Computer vision system for traffic sign recognition and overspeed alerts.",
        "full_description": "AI-based traffic safety system using OpenCV and TensorFlow Lite for real-time speed sign detection, comparing detected limits with vehicle speed, and alerting drivers when overspeeding.",
        "technologies": ["Python", "OpenCV", "TensorFlow", "Computer Vision", "AI"],
        "image": "speed-detection.jpg",
        "github": "#",
        "demo": "#",
        "category": "AI & Computer Vision",
        "status": "Research",
        "icon": "traffic-light"
    }
]

@app.route('/')
def index():
    current_year = datetime.now().year
    featured_projects = [p for p in projects if p['id'] in [1, 2, 3]]
    return render_template('index.html', 
                         featured_projects=featured_projects,
                         current_year=current_year)

@app.route('/projects')
def projects_page():
    return render_template('projects.html', projects=projects)

@app.route('/project/<int:project_id>')
def project_detail(project_id):
    project = next((p for p in projects if p['id'] == project_id), None)
    if project is None:
        flash('Project not found!', 'error')
        return redirect(url_for('projects_page'))
    return render_template('project_detail.html', project=project)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        
        if not name or not email or not message:
            flash('Please fill in all fields.', 'error')
            return render_template('contact.html')
        
        # Print to console (in real app, save to DB or send email)
        print(f"New message from {name} ({email}): {message}")
        flash('Thank you for your message! I will get back to you soon.', 'success')
        return redirect(url_for('contact'))
    
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)