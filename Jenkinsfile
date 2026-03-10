pipeline {

    agent any

    environment {
        ENV = "qa"
    }

    stages {

        stage('Checkout Code') {
            steps {
                git branch: 'main', url: 'https://github.com/diptimayadhal/playwright-pytest-framework.git'
            }
        }

        stage('Setup Python Environment') {
            steps {
                sh '''
                python3 -m venv venv
                . venv/bin/activate
                pip install --upgrade pip
                pip install -r requirements.txt
                python -m playwright install
                '''
            }
        }

        stage('Run Smoke Tests') {
            steps {
                script {
                    try {
                        sh '''
                        . venv/bin/activate
                        python -m pytest -m smoke -n 4 --env=$ENV --alluredir=allure-results
                        '''
                    } catch (Exception e) {
                        echo "Tests failed but continuing pipeline"
                    }
                }
            }
        }

        stage('Generate Allure Report') {
            steps {
                sh '''
                allure generate allure-results -o allure-report --clean
                '''
            }
        }

        stage('Archive Reports') {
            steps {
                archiveArtifacts artifacts: 'allure-report/**'
            }
        }

    }

}