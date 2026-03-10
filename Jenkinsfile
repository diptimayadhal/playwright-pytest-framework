pipeline {

    agent any

    stages {

        stage('Checkout Code') {
            steps {
                git 'https://github.com/diptimayadhal/playwright-pytest-framework.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
                sh 'playwright install'
            }
        }

        stage('Run Smoke Tests') {
            steps {
                sh 'pytest -m smoke -n 4'
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