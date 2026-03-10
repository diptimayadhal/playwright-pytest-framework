pipeline {

    agent any

    stages {

        stage('Checkout Code') {
            steps {
                git branch: 'main', url: 'https://github.com/diptimayadhal/playwright-pytest-framework.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip3 install -r requirements.txt'
                sh 'python3 -m playwright install'
            }
        }

        stage('Run Smoke Tests') {
            steps {
                sh 'python3 -m pytest -m smoke -n 4'
            }
        }

        stage('Generate Allure Report') {
            steps {
                sh 'allure generate reports -o allure-report'
            }
        }

        stage('Archive Reports') {
            steps {
                archiveArtifacts artifacts: 'allure-report/**'
            }
        }

    }
}