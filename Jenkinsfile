pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/venkatadurgaraoponnaganti/jenkins-python-demo.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                # Create & activate isolated virtual environment
                python3 -m venv venv
                . venv/bin/activate

                # Upgrade pip and install requirements
                python -m pip install --upgrade pip --break-system-packages
                python -m pip install --break-system-packages -r requirements.txt
                '''
            }
        }

        stage('Test') {
            steps {
                sh '''
                . venv/bin/activate
                pytest -v test_app.py
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
