pipeline {

    agent any

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
                sh '''
                . venv/bin/activate
                python -m pytest -m smoke -n 4
                '''
            }
        }

        stage('Generate Allure Report') {
            steps {
                sh '''
                allure generate reports -o allure-report
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