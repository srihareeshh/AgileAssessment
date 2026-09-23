pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/srihareeshh/AgileAssessment.git'
            }
        }
        stage('Parallel Checks') {
            parallel {
                stage('Frontend Check') {
                    steps {
                        bat 'python frontend_check.py'
                    }
                }
                stage('Archive Report') {
                    steps {
                        archiveArtifacts artifacts: 'frontend_report.txt', fingerprint: true
                    }
                stage('Backend Check') {
                    steps {
                        bat 'python backend_check.py'
                    }
                }
                stage('Archive Report') {
                    steps {
                        archiveArtifacts artifacts: 'backend_report.txt', fingerprint: true
                    }
            }
        }
        stage('Summary') {
            steps {
                echo 'Both frontend and backend checks are complete'
            }
        }
    }
}