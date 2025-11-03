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
                python3 -m venv venv
                . venv/bin/activate
                pip install -r requirements.txt
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
                echo 'Build and Test Completed Successfully!'
            }
        }
    }
}
