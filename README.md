<h1>Simple autotests on Python + Pytest + Selenium</h1>

This is simple test framework to create and run UI tests on python 3.7v for amazon.com
unit test tool: pytest.

Test framework has browser factory and page object pattern.

<h2>Running tests:</h2>
<ol>
  <li>Create project folder - <code>mkdir testfolder && cd path/to/testfolder</code></li>
  <li>Create environment - <code>python3 -m venv env</code></li>
  <li>Get librarys - <code>pip install -r requirements.txt</code></li>
  <li>Run tests <code>
  py.test test_mod.py   # run tests in module </code> <br>
  <code>py.test somepath      # run all tests below somepath</li></code>
</ol>

<h3>Attention:</h3>
Amazom can change element locators, page structure, and browser drivers can be updated - in this case, they will need to be updated.
