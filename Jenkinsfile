pipeline {
    agent any

    environment {
        PROJECT = "jenkins-python-demo"
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
                    echo "Creating virtual environment..."
                    python3 -m venv venv

                    echo "Activating virtual environment..."
                    . venv/bin/activate

                    echo "Fixing pip..."
                    curl -sS https://bootstrap.pypa.io/get-pip.py -o get-pip.py
                    python get-pip.py pip==23.3.2

                    echo "Installing dependencies..."
                    pip install -r requirements.txt

                    echo "Fixing permissions..."
                    chmod -R 755 venv
                '''
            }
        }

        stage('Test') {
            steps {
                sh '''
                    echo "Running unit tests..."
                    chmod +x venv/bin/pytest
                    venv/bin/python3 -m pytest -v test_app.py
                '''
            }
        }

        stage('Build Docker Image') {
            steps {
                sh '''
                    echo "Building Docker image..."
                    docker build -t pvdr8978/jenkins-python-demo:latest .
                '''
            }
        }

        stage('Push Docker Image') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub-credentials', usernameVariable: 'USERNAME', passwordVariable: 'PASSWORD')]) {
                    sh '''
                        echo "$PASSWORD" | docker login -u "$USERNAME" --password-stdin
                        docker push pvdr8978/jenkins-python-demo:latest
                    '''
                }
            }
        }
   



	stage('Deploy to EC2') {
    		steps {
        	sshagent(credentials: ['keypair']) {
            	sh '''
            	ssh -o StrictHostKeyChecking=no ubuntu@<13.201.193.47> '
                docker pull pvdr8978/jenkins-python-demo:latest &&
                docker run -d -p 5000:5000 pvdr8978/jenkins-python-demo:latest
            '
            '''
        }
    }
}
 }

    post {
        success {
            echo "✅ Build and tests successful!"
        }
        failure {
            echo "❌ Pipeline failed! Check the logs for errors."
        }
    }
}
