pipeline {
    agent any

    environment {
        VENV_NAME = 'virtual-coffee-shop'
    }

    stages {
        stage('Checkout and Deploy Flask App') {
            steps {
                script {
                    // Clone the repository
                    git branch: 'main', credentialsId: '897657d4-cafd-4ace-a03f-c69b3e2d16ff', url: 'https://github.com/musangisilvia/virtual-coffeeShop'

                    // Create and activate the virtual environment
                    sh "python3 -m venv ${VENV_NAME}"
                    sh "source ${VENV_NAME}/bin/activate && pip install -r requirements.txt"

                    // Assuming your Flask app entry point is app.py
                    sh "source ${VENV_NAME}/bin/activate && python app.py &"
                }
            }
        }
    }
}
