pipeline {
    parameters {
        choice(name: 'ACT', choices: ['A1', 'A2', 'A3', 'A4'], description: 'The Act to be analyzed for FPS performance')
        choice(name: 'CALC_TYPE', choices: ['minmax', 'avg'], description: 'The calculation type to be used for analyzing FPS performance')
        string(name: 'LOGS_DIR', defaultValue: './FPSLogs', description: 'The directory containing the FPS logs')
    }

    agent any

    stages {
        stage('Version') {
            steps {
                sh 'python3 --version'
            }
        }
        stage('FPS Analysis') {
            steps {
                echo "Build parameters: Act = ${params.ACT} | Calculation type = ${params.CALC_TYPE} | Logs directory = ${params.LOGS_DIR}"
                sh 'python3 d3fps.py' ${params.ACT} ${params.CALC_TYPE} ${params.LOGS_DIR}
            }
        }
    }
}
