 package com.lesfurets.jenkins

import org.junit.Before
import org.junit.Test

import com.lesfurets.jenkins.unit.BasePipelineTest

import static com.lesfurets.jenkins.unit.MethodCall.callArgsToString
import static org.junit.Assert.assertTrue

@Test 
void run_wihtout_errors() throws Exceptins {
    def script = runScript("src/ci_execute_send")
    script.execute()
    pritCallStack()
    assertJobStatusSuccess()
}

