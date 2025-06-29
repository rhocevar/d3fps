pipeline {
    parameters {
        string(name: 'Logs_directory', defaultValue: './FPSLogs', description: 'The directory containing the FPS logs')
        choice(name: 'Act', choices: ['A1', 'A2', 'A3', 'A4'], description: 'The Act to be analyzed for FPS performance')
        choice(name: 'Calculation_type', choices: ['minmax', 'avg'], description: 'The calculation type to be used for analyzing FPS performance')
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
                sh 'python3 d3fps.py ${params.Act} ${params.Calculation_type} ${params.Logs_directory}'
            }
        }
    }
}
