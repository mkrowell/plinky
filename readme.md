# Usage:

After setting up a PuTTY saved session (e.g., foo), plinky can be used as follows:

```python
import plinky

# connect to a remote server using the PuTTY session named "foo"
plinky.start("foo")

# test whether there is a process listening on local port 1722
plinky.test_connection(1722)

# test whether there is a process listening on local port 1722
plinky.stop()
```

# Details
* **plinky.start**(*profile*) Opens a connection to the remote server with the saved
	session profile *"profile"*. An exception is raised if the process fails to
	start, but not necessarily if the connection fails.

* **plinky.test_connection**(*port, host = "127.0.0.1"*) Tests if a connection
	exists at the specified `port` and `host`. The host defaults to [localhost].

* **plinky.stop**() Closes the current plink session by calling the
	`kill()` method of the subprocess in which plink is running.
	Note that calling `plinky.stop()` does not cause the connection to be
	closed immediately, and as such, the call to `test_connection()` in the
	following snippet may return `True`:

```python
import plinky
plinky.start("foo")
plinky.stop()
plinky.test_connection()
```

# Quirks

For now, plinky only supports a single SSH session; calling
'plinky.start("foo"); plinky.start("bar");' will cause the SSH session to
"foo" to be closed before the connection with "bar" is opened.
