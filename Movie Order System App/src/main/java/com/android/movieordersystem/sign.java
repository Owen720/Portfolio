package com.android.movieordersystem;


import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;
import android.widget.Toast;

import androidx.annotation.NonNull;
import androidx.appcompat.app.AppCompatActivity;

import com.google.android.gms.tasks.OnCompleteListener;
import com.google.android.gms.tasks.Task;
import com.google.firebase.auth.AuthResult;
import com.google.firebase.auth.FirebaseAuth;

public class sign extends AppCompatActivity {
    EditText emailId, password;
    Button btnSignUp, back, fb, google;
    TextView tvSignIn, login;
    FirebaseAuth mFirebaseAuth;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.sign_up_page);

        mFirebaseAuth = FirebaseAuth.getInstance();
        emailId = findViewById(R.id.enter_name);
        password = findViewById(R.id.enter_password);
        btnSignUp = findViewById(R.id.sign);
        tvSignIn = findViewById(R.id.login);
        btnSignUp.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                String email = emailId.getText().toString();
                String pwd = password.getText().toString();
                if(email.isEmpty()){
                    emailId.setError("Please enter email id");
                    emailId.requestFocus();
                }
                else  if(pwd.isEmpty()){
                    password.setError("Please enter your password");
                    password.requestFocus();
                }
                else  if(email.isEmpty() && pwd.isEmpty()){
                    Toast.makeText(sign.this,"Fields Are Empty!",Toast.LENGTH_SHORT).show();
                }
                else  if(!(email.isEmpty() && pwd.isEmpty())){
                    mFirebaseAuth.createUserWithEmailAndPassword(email, pwd).addOnCompleteListener(sign.this, new OnCompleteListener<AuthResult>() {
                        @Override
                        public void onComplete(@NonNull Task<AuthResult> task) {
                            if(!task.isSuccessful()){
                                Toast.makeText(sign.this,"Sign Up Unsuccessful, Please Try Again",Toast.LENGTH_SHORT).show();
                            }
                            else {
                                Toast.makeText(sign.this,"Sign Up USuccessful!",Toast.LENGTH_SHORT).show();
                                startActivity(new Intent(sign.this,login.class));
                            }
                        }
                    });
                }
                else{
                    Toast.makeText(sign.this,"Error Occurred!",Toast.LENGTH_SHORT).show();

                }
            }
        });

        tvSignIn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent i = new Intent(sign.this,login.class);
                startActivity(i);
            }
        });
        back = findViewById(R.id.back);
        back.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent intent = new Intent(sign.this, LoginOrRegister.class);
                startActivity(intent);
            }
        });

        login = (TextView) findViewById(R.id.login);
        login.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent intent = new Intent(sign.this, login.class);
                startActivity(intent);
            }
        });

        fb = findViewById(R.id.fb_sign);
        fb.setOnClickListener(new View.OnClickListener() {
            public void onClick(View v) {
                server_down();
            }
        });

        google = findViewById(R.id.google_sign);
        google.setOnClickListener(new View.OnClickListener() {
            public void onClick(View v) {
                server_down();
            }
        });
    }

    public void server_down() {
        Toast.makeText(sign.this,"Sorry! Server maintenance, Please try again later!",Toast.LENGTH_SHORT).show();
    }
}

