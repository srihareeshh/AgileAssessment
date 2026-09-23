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
                stage('Frontend Execution') {
                    steps {
                        bat 'python frontend_check.py'
                        archiveArtifacts artifacts: 'frontend_report.txt', fingerprint: true
                    }
                }
                stage('Backend Execution') {
                    steps {
                        bat 'python backend_check.py'
                        archiveArtifacts artifacts: 'backend_report.txt', fingerprint: true
                    }
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
