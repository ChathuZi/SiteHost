Hi Alice,

Thanks for reaching out. I’ve investigated the issue with your website, **site.recruitment.shq.nz**, and found that it is not resolving correctly due to a DNS configuration problem.

Specifically, your domain does not have an **A record** pointing to the server’s IP address `120.138.30.179`. Because of this, browsers are unable to locate your website using the domain name. However, the server itself is up and running, and the site is accessible directly via the IP address when the correct `Host` header is used.

To temporarily view the site, you can:

1. Open your system's terminal or command prompt.
2. Edit your `hosts` file to add the following line:
120.138.30.179 site.recruitment.shq.nz

3. Save the file and visit `http://site.recruitment.shq.nz` in your browser.

After doing this, I was able to access the site and retrieve the following hidden code from the HTML `<head>` section:

<!-- This is what you're looking for: R2F1ci9FK0pYK2dFcWd4YWZ4QlplaXVCYmNnTWJCeWtNdDhud3lFVlg5az0= -->

To resolve this permanently, you’ll need to update the DNS settings for your domain by adding an A record like:

- **Name**: `site.recruitment.shq.nz`  
- **Type**: `A`  
- **Value**: `120.138.30.179`

This change should be made via your DNS hosting provider or domain registrar.

Let me know if you need any help coordinating this change .  I’m happy to assist further!

Best regards,  
**Sudeshinie Wadigawage**