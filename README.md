django-ajax-auth
================
This application provides simple Django authentication via AJAX calls. To include it in your application, checkout the project and add ```ajax_auth``` to your INSTALLED_APPS. See the example project fo full usage.

### Sample Usage
##### Login

```
$.post("ajax_auth/login/", $(form).serialize(),
    function (data) {
        // Result should be {"success": true}
      })
      .fail(function (err) {
        // Result will be {"error_msg":<message>,"success":false}
      });
```

##### Register

```
$.post("ajax_auth/register/", $(form).serialize(),
    function (data) {
        // Result should be {"success": true}
      })
      .fail(function (err) {
        // Result will be {"error_msg":<message>,"success":false}
      });
```

##### Logout

```
$.post("ajax_auth/logout/", $(form).serialize(),
    function (data) {
        // Result should be {"success": true}
      })
```

