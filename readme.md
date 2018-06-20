# Usage
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

# Setting up PuTTY Session
SSH tunnels are created by PuTTY, a free, open source SSH client, which can be obtained from the PuTTY downloads page. Once downloaded, open the configuration window. Within the configuration window, use the Category selector on the left to expand the connection node, then SSH nodes, and select the Auth pane. On the Auth pane, click the Browse button and select the private key for your remote instance.
 
To set up an SSH-tunnel (i.e. port forwarding) to the database servers, map the local ports to ports on the remote instances. In the Category selector select the SSH/Tunnels pane, and enter the source and destination ports.

Next, navigate to the Session pane at the top of the Category selector, and enter the Host Name you wish to connect to.

Finally, give a name to the settings profile you've created in the Saved Sessions field and click Save. 

# Quirks

For now, plinky only supports a single SSH session; calling
'plinky.start("foo"); plinky.start("bar");' will cause the SSH session to
"foo" to be closed before the connection with "bar" is opened.
