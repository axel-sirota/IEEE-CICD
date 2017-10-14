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


        stage('Compile') {
            timeout(time: 30, unit: 'SECONDS') {
                sh "${pythonExecutable} -m compileall -f -q funniest"
            }
        }

        stage('Build .whl & .tar.gz') {
            sh "${pythonExecutable} setup.py bdist_wheel"
        }

        stage('Install dependencies') {
            sh "${pythonExecutable} -m pip install -U --quiet ."
        }

        stage('Unit Tests') {
            timestamps {
                timeout(time: 30, unit: 'MINUTES') {
                    try {
                        sh "${pythonExecutable} setup.py nosetests --verbose --with-xunit --xunit-file=output/xunit.xml --with-xcoverage --xcoverage-file=output/coverage.xml --cover-package=funniest --cover-erase --tests tests/units"
                    } finally {
                        step([$class: 'JUnitResultArchiver', testResults: 'output/xunit.xml'])
                        step([$class: 'CoberturaPublisher', autoUpdateHealth: false, autoUpdateStability: false, coberturaReportFile: 'output/coverage.xml', failUnhealthy: true, failUnstable: true, maxNumberOfBuilds: 0, onlyStable: true, sourceEncoding: 'ASCII', zoomCoverageChart: true])
                    }
                }
            }
        }

        stage('Code checking') {

            sh "${pythonExecutable} -m pylint --output-format=parseable --reports=y funniest > output/pylint.log || exit 0"
            sh "${pythonExecutable} -m flake8 --exit-zero --output-file=output/flake8.log funniest"
        }


        stage('Archive build artifact: .whl , .tar.gz and reports') {
            archive 'dist/*'
            archive 'output/*'
        }

        stage('Clean all'){
            sh 'rm -rf temp'
        }

}
