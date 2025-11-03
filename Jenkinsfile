pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/venkatadurgaraoponnaganti/jenkins-python-demo.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                # Create and activate virtual environment
                python3 -m venv venv
                . venv/bin/activate

                # Upgrade pip and install dependencies safely (Ubuntu 24.04 fix)
                pip install --upgrade pip
                pip install --break-system-packages -r requirements.txt
                '''
            }
        }

        stage('Test') {
            steps {
                sh '''
                . venv/bin/activate
                pytest test_app.py
                '''
            }
        }

        stage('Build Complete') {
            steps {
                echo '✅ Build and Test Completed Successfully!'
            }
        }
    }
}
