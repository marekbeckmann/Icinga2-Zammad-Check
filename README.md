# Zammad Icinga2 Checks

## 1. Functionality

This plugin gives you the ability, to display the Zammad Monitoring Status within Icinga2, using the Zammad API. 

## 2. Script Usage:

Clone this repository, and copy the `check_zammad.py` script to your Icinga2 Plugin Directory.
You may need to grant the script permission and assign the correct owner.

```bash
git clone https://github.com/marekbeckmann/Icinga2-Zammad-Check zammad-icinga2-checks
cd zammad-icinga2-checks
cp check_zammad.py /usr/lib/nagios/plugins/
chmod +x /usr/lib/nagios/plugins/check_zammad.py
chown nagios /usr/lib/nagios/plugins/check_zammad.py
```

To execute the script, run the following command: 
```bash
python3 check_zammad.py <args>
```

You can run the script with the following arguments: 
| argument                | Required | description                |
| ----------------------- | -------- | -------------------------- |
| `-h`                    | ❌        | Show help message and exit |
| `--server`   `<url>`    | ✅        | URL of Zammad instance     |
| `--token`     `<token>` | ✅        | Token                      |

You can get the token from here: https://zammad.example.org/#system/monitoring

**Important:** The Server URL mustn't end with a slash. E.g: https://zammad.example.org

## 2. Icinga Config (example):

`services.conf`
```
apply Service "zammadcheck" {
  import "generic-service"
  check_command = "check-zammad"
  assign where host.name == "zammad-server"
}
```

`commands.conf`
```
object CheckCommand "check-zammad" {
  import "plugin-check-command"

  command = [PluginDir + "/check_zammad"]

    arguments = {
      "--server" = "SERVER_URL"
      "--token" =  "TOKEN"
    }
}
```

---

## Sample Output: 
```bash
$ python3 check_zammad.py --server example.zammad.org --token 12345
```
```ini
Zammad Health Message:
Issues: No issues
Actions: No actions
```
