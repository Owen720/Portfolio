package com.android.movieordersystem;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;

import androidx.appcompat.app.AppCompatActivity;


public class LoginOrRegister extends AppCompatActivity {
    private Button login;
    private Button sign;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.login_or_register);

        login = findViewById(R.id.LOGIN);
        login.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                go_login();
            }
        });

        sign = findViewById(R.id.Sign);
        sign.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                sign_up();
            }
        });
    }

    public void go_login() {
        Intent intent = new Intent(LoginOrRegister.this, login.class);
        startActivity(intent);
    }

    public void sign_up() {
        Intent intent = new Intent(LoginOrRegister.this, sign.class);
        startActivity(intent);
    }
}