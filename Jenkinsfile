pipeline {
    agent any

    options {
        timestamps()
    }

    environment {
        APP_NAME = "project-phoenix"
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
                echo "Checked out repository for ${env.APP_NAME}"
            }
        }

        stage('Build') {
            steps {
                echo "Build stage started"
                // Simulated build output
                bat '''
                if not exist dist mkdir dist
                echo BUILD OK > dist\\build.txt
                '''
            }
        }

        stage('Test') {
            steps {
                echo "Test stage started"
                // Simulated test result
                bat '''
                if not exist results mkdir results
                echo TESTS PASSED > results\\test-results.txt
                '''
            }
        }

        stage('Deploy') {
            steps {
                echo "Deploy stage started (only runs if previous stages pass)"
                // Simulated deploy log
                bat '''
                if not exist deploy mkdir deploy
                echo DEPLOYED OK > deploy\\deploy-log.txt
                '''
            }
        }
    }

    post {
        success {
            echo "✅ Pipeline SUCCESS: Build, Test, Deploy completed"
        }
        failure {
            echo "❌ Pipeline FAILED: stopping at the failed stage"
        }
        always {
            echo "📦 Archiving artifacts..."
            archiveArtifacts artifacts: 'dist/**, results/**, deploy/**', fingerprint: true
        }
    }
}
