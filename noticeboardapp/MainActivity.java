package com.example.thoufeeq.smartnoticeboard;

import android.content.ActivityNotFoundException;
import android.content.Intent;
import android.speech.RecognizerIntent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

import java.util.ArrayList;
import java.util.Locale;
import java.util.Properties;

import javax.mail.PasswordAuthentication;
import javax.mail.Session;


public class MainActivity extends AppCompatActivity implements View.OnClickListener {

    public EditText resultedTEXT;
    //Declaring EditText
    private EditText editTextMessage;

    //Send button
    private Button buttonSend;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        //Initializing the views
        resultedTEXT = (EditText) findViewById(R.id.editTextMessage);

        buttonSend = (Button) findViewById(R.id.buttonSend);

        //Adding click listener
        buttonSend.setOnClickListener(this);
    }

    // Speech Recognition

    public void onButtonClick(View v)
    {
        if(v.getId() == R.id.imageButton)
        {

            promptSpeechInput();
        }
    }

    public void promptSpeechInput() {
        Intent i = new Intent(RecognizerIntent.ACTION_RECOGNIZE_SPEECH);
        i.putExtra(RecognizerIntent.EXTRA_LANGUAGE_MODEL, RecognizerIntent.LANGUAGE_MODEL_FREE_FORM);
        i.putExtra(RecognizerIntent.EXTRA_LANGUAGE, Locale.getDefault());
        i.putExtra(RecognizerIntent.EXTRA_PROMPT, "Say something");

        try {
            startActivityForResult(i, 100);
        }
        catch(ActivityNotFoundException a)
        {
            Toast.makeText(MainActivity.this, "Sorry! Your device does not support speech", Toast.LENGTH_LONG).show();
        }
    }

    public void onActivityResult(int request_code, int result_code, Intent i)
    {
        super.onActivityResult(request_code, result_code, i);

        switch(request_code)
        {
            case 100: if(result_code == RESULT_OK && i != null)
            {
                ArrayList<String> result = i.getStringArrayListExtra(RecognizerIntent.EXTRA_RESULTS);
                resultedTEXT.setText(result.get(0));

            }
                break;
        }
    }

    // end


    private void sendEmail() {
        
        String email = "thoufeeq.mohd@gmail.com";
        String subject = "New Notification!";
        String message = resultedTEXT.getText().toString();

        //Creating SendMail object
        SendMail sm = new SendMail(this, email, subject, message);

        //Executing sendmail to send email
        sm.execute();
    }

    @Override
    public void onClick(View v) {
        sendEmail();
    }
}
