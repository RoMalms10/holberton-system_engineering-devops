# Postmortem

## Issue Summary
A problem with the servers was uncovered after a recent update. This resulted in an outage for an hour (00:00 UTC - 01:00 UTC). The impact of this outage was devastating. The service was completely down for 100% of users for 15 minutes before a backup server was brought online with the previous version. The root cause of the issue was a typo in the settings file in the NGINX configuration.

## Timeline
* 00:00 UTC - Update applied
* 00:05 UTC - Fatal outages noticed by monitoring system, customer complaints rolling in, SRE team on-call contacted
* 00:06 UTC - Backup server being brought online
* 00:15 UTC - Backup server generated
* 00:20 UTC - Issue being looked into
* 00:25 UTC - Issue discovered
* 00:30 UTC - Fix created and being rolled out to faulty servers
* 00:50 UTC - Fix issued to all faulty servers, switching from backup server to regular servers
* 01:00 UTC - Fix completed

## Root Cause
After the most recent update, the servers became faulty. Upon inspection it was noticed that the servers were failing to launch NGINX. The SRE team on call discovered that the settings file was trying to load a file with the extension `.phpp` when the correct extension was `.php`.

## Corrective and preventative measures
Broadly speaking, more attention to detail should be exercised when editing the settings in the servers. <br>
**Some tasks that could lead to prevention of the same mistake:**
* Create a script that checks the settings file for typos.
* Test in development environment more before pushing to live.
