package org.zalando;

import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.security.Principal;

@RestController
public class HelloworldController {

    @RequestMapping("/hello")
    public String sayHello(Principal principal) {
        return "Hello " + principal.getName() + "!";
    }
}
