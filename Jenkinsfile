#!/usr/bin/env groovy

def pythonExecutable = '$WORKSPACE/temp/bin/python3'
def testPypi = 'https://test.pypi.org/legacy/'

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
                sh "${pythonExecutable} -m compileall -f -q funniest_ieee"
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
                        sh "${pythonExecutable} setup.py nosetests --verbose --with-xunit --xunit-file=output/xunit.xml --with-xcoverage --xcoverage-file=output/coverage.xml --cover-package=funniest_ieee --cover-erase --tests tests"
                    } finally {
                        step([$class: 'JUnitResultArchiver', testResults: 'output/xunit.xml'])
                        step([$class: 'CoberturaPublisher', autoUpdateHealth: false, autoUpdateStability: false, coberturaReportFile: 'output/coverage.xml', failUnhealthy: true, failUnstable: true, maxNumberOfBuilds: 0, onlyStable: true, sourceEncoding: 'ASCII', zoomCoverageChart: true])
                    }
                }
            }
        }

        stage('Code checking') {

            sh "${pythonExecutable} -m pylint --output-format=parseable --reports=y funniest_ieee > output/pylint.log || exit 0"
            sh "${pythonExecutable} -m flake8 --exit-zero --output-file=output/flake8.log funniest_ieee"
                        step([
                $class                     : 'WarningsPublisher',
                parserConfigurations       : [[parserName: 'PYLint', pattern   : 'output/pylint.log']],
                unstableTotalAll           : '20',
                usePreviousBuildAsReference: true
            ])
            step([
                $class                     : 'WarningsPublisher',
                parserConfigurations       : [[parserName: 'Flake8', pattern   : 'output/flake8.log']],
                unstableTotalAll           : '20',
                usePreviousBuildAsReference: true
            ])
        }


        stage('Archive build artifact: .whl , .tar.gz and reports') {
            archive 'dist/*'
            archive 'output/*'
        }
        stage('Deploy to Pypi?') {
        input('Deploy to Pypi?')
        }

        stage('Deploy to Pypi') {
            sh "export TWINE_REPOSITORY_URL=${testPypi}"
            sh "export TWINE_REPOSITORY=${testPypi}"
            sh "export TWINE_PASSWORD=IEEE-CICDPython"
            sh "export TWINE_USERNAME=axel.sirota"
            sh "${pythonExecutable} -m twine upload --config-file .pypirc -r test dist/funniest_ieee-0.4-py2.py3-none-any.whl"
        }

        stage('Clean all'){
            sh 'rm -rf temp'
        }

}
