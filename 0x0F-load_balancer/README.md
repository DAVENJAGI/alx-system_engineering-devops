0x0F-load_balancer.
===================

* Configuring a server and adding  a load balancer to enhance redundancy...

*Task 1
========
Configure web-02 server to be identicle to web-01.
We want to add a custom nginx reponse header.

-Configure nginx such that it HTTP response contains a custom header on web-01 and web-01
-Name of the custome header must be x-served-BY
-Value of the custom HTTP header must be the host name of the server nginx is running on.

*Task 2
========
Install and configure HAProxy on 1b-01 server.
COnfigure HAProxy to send traffic to the web-01 and web-02
Distribute requests using round robin algorithm
Make sure HAProxy can be managed using an init script
Make sure servers are config with correct host names, ie, [STUDENT_ID]-web-01 and [STUDENT_ID]-web-02
For the answer file write a bash script that configures a new ubuntu machine wrt the above requirements.
