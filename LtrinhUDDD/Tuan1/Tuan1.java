package Tuan1;package Tuan1;

import android.os.Bundle;
import android.widget.Button;
import android.widget.EditText;

import androidx.activity.EdgeToEdge;
import androidx.appcompat.app.AppCompatActivity;
import androidx.core.graphics.Insets;
import androidx.core.view.ViewCompat;
import androidx.core.view.WindowInsetsCompat;

import com.example.ungdung.R;

public class Tuan1 extends AppCompatActivity {
    // Khai bao bien
    EditText edt1,edt2,edt3;
    Button tong;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        // Anh xa cac control
        edt1 = findViewById(R.id.edtA);
        edt2 = findViewById(R.id.edtB);
        edt3 = findViewById(R.id.edtKQ);
        tong = findViewById(R.id.btnTong);
        // Xu ly cac su kien
        tong.setOnClickListener(v->{
            // goi ham tinh tong
            TinhTong();
        });
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_tuan1);

    }
    // Dinh nghia ham TinhTong
    private void TinhTong() {
        // Lay du lieu tu edtA
        String str1=edt1.getText().toString();  // Lay du lieu text dang String
        float so1=Float.parseFloat(str1);       // Chuyen tu kieu String sang kieu so
        // Lam tuong tu voi edtB
        String str2=edt2.getText().toString();
        float so2=Float.parseFloat(str2);
        // Tinh Tong
        float Tong=so1+so2;
        // In ket qua ra man hinh
        edt3.setText(String.valueOf(Tong));
    }
}