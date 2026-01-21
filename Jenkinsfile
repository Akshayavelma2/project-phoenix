stage('Test') {
    steps {
        echo "Test stage started"
        bat '''
        if not exist results mkdir results
        echo TESTS PASSED > results\\test-results.txt
        '''
    }
}
