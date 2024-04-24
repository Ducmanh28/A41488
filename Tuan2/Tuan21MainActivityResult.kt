package com.example.ungdungtinhtong21.tuan2

import android.content.Intent
import android.os.Bundle
import android.widget.TextView
import androidx.activity.enableEdgeToEdge
import androidx.appcompat.app.AppCompatActivity
import androidx.core.view.ViewCompat
import androidx.core.view.WindowInsetsCompat
import com.example.ungdungtinhtong21.R

class Tuan21MainActivityResult : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        enableEdgeToEdge()
        setContentView(R.layout.activity_tuan21_main_result)
        ViewCompat.setOnApplyWindowInsetsListener(findViewById(R.id.main)) { v, insets ->
            val systemBars = insets.getInsets(WindowInsetsCompat.Type.systemBars())
            v.setPadding(systemBars.left, systemBars.top, systemBars.right, systemBars.bottom)
            insets
        }
        var tvKQ=findViewById<TextView>(R.id.tuan2KQ)
        val i1=intent
        val chuoi1= i1.extras!!.getString("so1")
        val so1=chuoi1!!.toFloat()
        val chuoi2= i1.extras!!.getString("so2")
        val so2=chuoi2!!.toFloat()

        val tong=so1+so2
        tvKQ!!.text=tong.toString()
    }
}