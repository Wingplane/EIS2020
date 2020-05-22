package com.example.lianxi0520_1;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.os.Handler;
import android.os.Message;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;
import android.widget.Toast;

import java.text.SimpleDateFormat;

public class MainActivity extends AppCompatActivity {
    private TextView textView;
    private Button button,button5;
    boolean flag = false;
    int time_a = 0;
    Handler handler = new Handler() {
        public void handleMessage(Message msg) {
            if (msg.what == 0x01) {
                textView.setText("计时器:" + msg.obj.toString());
                //Toast.makeText(MainActivity.this, "计时器:" + msg.obj.toString(), Toast.LENGTH_SHORT).show();
            }
            if (msg.what == 0x02) {
                textView.setText("22222222");
            }
        }
    };

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        flag = true;
        textView = findViewById(R.id.textView);
        button = (Button) findViewById(R.id.button);
        button5 = (Button) findViewById(R.id.button5);
        new Thread() {
            public void run() {
                while (flag) {
                    time_a = time_a + 1;
                    SimpleDateFormat format = new SimpleDateFormat("yyyy年MM月dd HH:mm:ss");
                    String timeStr = format.format(System.currentTimeMillis());
                    Message msg = new Message();
                    msg.what = 0x01;
                    msg.obj = timeStr;
                    //msg.obj = time_a;
                    handler.sendMessage(msg);
                    try {
                        Thread.sleep(1000);
                    } catch (InterruptedException e) {
                        e.printStackTrace();
                    }
                }
            }
        }.start();
       button5.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent back=new Intent(MainActivity.this,Main3Activity.class);
                startActivity(back);
            }
        });
       button.setOnClickListener(new View.OnClickListener() {
           @Override
           public void onClick(View v) {
               Intent back1 = new Intent(MainActivity.this,Main2Activity.class);
               startActivity(back1);
           }
       });
    }
}