+import modules
+
+def test_news():
+    assert('wake' == modules.process_query('I want to wake up at 07:21')[0])
+    assert('wake' == modules.process_query('wake up at 10:20')[0])
+    assert('wake' == modules.process_query('wake up')[0])
+    assert('wake' != modules.process_query('something random')[0])