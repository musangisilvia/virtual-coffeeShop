pipeline {
    agent any

    environment {
        VENV_NAME = 'virtual-coffee-shop'
        CONFIG_FILE = 'config.py'
    }

    stages {
        stage('Checkout and Build Flask App') {
            steps {
                script {
                    // Clone the repository
                    git branch: 'main', credentialsId: '897657d4-cafd-4ace-a03f-c69b3e2d16ff', url: 'https://github.com/musangisilvia/virtual-coffeeShop'

                    // Create and activate the virtual environment
                    sh "python3 -m venv ${VENV_NAME}"
                    
                    // Activate the virtual environment and install dependencies
                    withEnv(["PATH+VENV=${env.WORKSPACE}/${VENV_NAME}/bin"]) {
                        sh "pip install -r requirements.txt"
                    }
                }
            }
        }

        stage('Deploy Flask App') {
            steps {
                script {
                    // Copy config.py to the Flask app's working directory
                    sh "cp ~/${CONFIG_FILE} ${env.WORKSPACE}/${VENV_NAME}/bin/"

                    // Start the Flask app in the background
                    sh "nohup ${VENV_NAME}/bin/python app.py > /dev/null 2>&1 &"
                }
            }
        }
    }
}
