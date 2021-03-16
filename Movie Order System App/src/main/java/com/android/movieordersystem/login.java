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
import com.google.firebase.auth.FirebaseUser;


public class login extends AppCompatActivity {
    private EditText email, pw;
    private Button fb, google, login, back;
    private TextView forget;
    Button fb1, google1;
    FirebaseAuth db;
    private FirebaseAuth.AuthStateListener dbStateLister;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.login_page);

        db = FirebaseAuth.getInstance();
        email = findViewById(R.id.enter_name);
        pw = findViewById(R.id.enter_password);
        login = findViewById(R.id.LOGIN);
        back = findViewById(R.id.back);
        fb = findViewById(R.id.fb);
        google = findViewById(R.id.google);
        fb1 = findViewById(R.id.login_with_fb);
        google1 = findViewById(R.id.login_with_google);
        forget = (TextView) findViewById(R.id.forget_pw);

        dbStateLister = new FirebaseAuth.AuthStateListener() {
            @Override
            public void onAuthStateChanged(@NonNull FirebaseAuth firebaseAuth) {
                FirebaseUser User = db.getCurrentUser();
                if (User != null) {
                    Toast.makeText(login.this, "You are logged in", Toast.LENGTH_SHORT).show();
                    Intent i = new Intent(login.this, MainMenu.class);
                    startActivity(i);
                } else {
                    Toast.makeText(login.this, "Please Login", Toast.LENGTH_SHORT).show();
                }
            }
        };
        login.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                String email1 = email.getText().toString();
                String pwd = pw.getText().toString();
                if (email1.isEmpty()) {
                    email.setError("Please enter email id");
                    email.requestFocus();
                } else if (pwd.isEmpty()) {
                    pw.setError("Please enter your password");
                    pw.requestFocus();
                } else if (email1.isEmpty() && pwd.isEmpty()) {
                    Toast.makeText(login.this, "Fields Are Empty!", Toast.LENGTH_SHORT).show();
                } else if (!(email1.isEmpty() && pwd.isEmpty())) {
                    db.signInWithEmailAndPassword(email1, pwd).addOnCompleteListener(login.this, new OnCompleteListener<AuthResult>() {
                        @Override
                        public void onComplete(@NonNull Task<AuthResult> task) {
                            if (!task.isSuccessful()) {
                                Toast.makeText(login.this, "Login Error, Please Login Again", Toast.LENGTH_SHORT).show();
                            } else {
                                Intent goMain = new Intent(login.this, MainMenu.class);
                                startActivity(goMain);
                            }
                        }
                    });
                } else {
                    Toast.makeText(login.this, "Error Occurred!", Toast.LENGTH_SHORT).show();

                }
            }
        });

        back = findViewById(R.id.back);
        back.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent intent = new Intent(login.this, LoginOrRegister.class);
                startActivity(intent);
            }
        });

        forget = (TextView) findViewById(R.id.forget_pw);
        forget.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                server_down();
            }
        });

        fb1 = findViewById(R.id.login_with_fb);
        fb.setOnClickListener(new View.OnClickListener() {
            public void onClick(View v) {
                server_down();
            }
        });

        fb = findViewById(R.id.fb);
        fb.setOnClickListener(new View.OnClickListener() {
            public void onClick(View v) {
                server_down();
            }
        });

        google1 = findViewById(R.id.login_with_google);
        google.setOnClickListener(new View.OnClickListener() {
            public void onClick(View v) {
                server_down();
            }
        });

        google = findViewById(R.id.google);
        google.setOnClickListener(new View.OnClickListener() {
            public void onClick(View v) {
                server_down();
            }
        });
    }

    public void server_down() {
        Toast.makeText(login.this, "Sorry! Server maintenance, Please try again later!", Toast.LENGTH_SHORT).show();
    }

    @Override
    protected void onStart() {
        super.onStart();
        db.addAuthStateListener(dbStateLister);
    }
}