pipeline {
    agent any

    environment {
        DOCKERHUB_CREDENTIALS = credentials('dockerhub-creds')
        IMAGE_NAME = 'venkatadurgaraoponnaganti/python-demo-app'
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/venkatadurgaraoponnaganti/jenkins-python-demo.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                # Create a fresh Python virtual environment
                python3 -m venv venv
                . venv/bin/activate

                # Pin pip to a stable version (avoid pip 25.x issues)
                python -m ensurepip
                python -m pip install --upgrade "pip==24.3.1" --break-system-packages

                # Install required Python dependencies
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

        stage('Build Docker Image') {
            steps {
                sh '''
                docker build -t $IMAGE_NAME:latest .
                '''
            }
        }

        stage('Push Docker Image') {
            steps {
                withDockerRegistry([ credentialsId: 'dockerhub-creds', url: '' ]) {
                    sh '''
                    docker tag $IMAGE_NAME:latest $IMAGE_NAME:${BUILD_NUMBER}
                    docker push $IMAGE_NAME:latest
                    docker push $IMAGE_NAME:${BUILD_NUMBER}
                    '''
                }
            }
        }

        stage('Build Complete') {
            steps {
                echo '✅ CI/CD Pipeline Completed Successfully!'
            }
        }
    }
}
