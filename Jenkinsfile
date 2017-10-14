#!/usr/bin/env groovy

def pythonExecutable = '$WORKSPACE/temp/bin/python3'

node {

        stage('Clean') {
            sh "rm -rf *"
            sh 'pip3 install virtualenv'
            sh 'virtualenv --no-site-packages -p $(which python3) temp'
            sh '. $WORKSPACE/temp/bin/activate'
            sh 'mkdir output'

        }

        stage('Checkout SCM') {
            git branch: 'master',
            url: 'https://github.com/axel-sirota/IEEE-CICD'
        }

        stage('Build .whl & .tar.gz') {
            sh "${pythonExecutable} setup.py bdist_wheel"
        }

        stage('Install dependencies') {
            sh "${pythonExecutable} -m pip install -U --quiet . nose"
        }

        stage('Unit Tests') {
            timestamps {
                timeout(time: 30, unit: 'MINUTES') {
                    sh "${pythonExecutable} setup.py nosetests --verbose --xunit-file=output/xunit.xml --tests tests"
                }
            }
        }

        stage('Archive build artifact: .whl , .tar.gz and reports') {
            archive 'dist/*'
            archive 'output/*'
        }

}
