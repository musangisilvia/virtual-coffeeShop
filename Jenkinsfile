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
                    
                    // Activate the virtual environment and install dependencies
                    withEnv(["PATH+VENV=${env.WORKSPACE}/${VENV_NAME}/bin"]) {
                        sh "pip install -r requirements.txt"
                    }

                    sh "nohup ${VENV_NAME}/bin/python app.py > /dev/null 2>&1 &"
                }
            }
        }
    }
}
