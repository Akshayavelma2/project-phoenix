pipeline {
    agent any

    options {
        timestamps()
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
                echo "Checked out source"
            }
        }

        stage('Build') {
            steps {
                echo "Build stage"
                bat '''
                if not exist dist mkdir dist
                echo BUILD OK > dist\\build.txt
                '''
            }
        }

        stage('Test') {
            steps {
                echo "Test stage"
                bat '''
                if not exist results mkdir results
                echo TESTS PASSED > results\\test-results.txt
                '''
            }
        }

        stage('Deploy') {
            steps {
                echo "Deploy stage"
                bat '''
                if not exist deploy mkdir deploy
                echo DEPLOYED OK > deploy\\deploy-log.txt
                '''
            }
        }
    }

    post {
        success {
            echo "✅ Pipeline SUCCESS"
        }
        failure {
            echo "❌ Pipeline FAILED"
        }
        always {
            echo "📦 Archiving artifacts"
            archiveArtifacts artifacts: 'dist/**,results/**,deploy/**', fingerprint: true
        }
    }
}
