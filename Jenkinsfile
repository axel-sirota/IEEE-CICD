#!/usr/bin/env groovy

node {

        stage('Clean') {
            sh "rm -rf *"
            sh 'mkdir output'
        }

        stage('Checkout SCM') {
            git branch: 'master',
            url: 'https://github.com/axel-sirota/IEEE-CICD'
        }

        stage('Build .whl & .tar.gz') {
            sh "bash run.sh python setup.py bdist_wheel"
        }

        stage('Install dependencies') {
            sh "bash run.sh  python -m pip install -U --quiet . nose"
        }

        stage('Unit Tests') {
            timestamps {
                timeout(time: 30, unit: 'MINUTES') {
                    sh "bash run.sh  python setup.py nosetests --verbose --xunit-file=output/xunit.xml --tests tests"
                }
            }
        }

        stage('Archive build artifact: .whl , .tar.gz and reports') {
            archive 'dist/*'
            archive 'output/*'
        }

}
