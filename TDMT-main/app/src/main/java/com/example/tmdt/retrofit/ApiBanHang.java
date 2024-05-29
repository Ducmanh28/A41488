package com.example.tmdt.retrofit;

import io.reactivex.rxjava3.core.Observable;
import com.example.tmdt.model.LoaiSpModel;
import com.example.tmdt.model.SanPhamMoiModel;

import retrofit2.http.Field;
import retrofit2.http.FormUrlEncoded;
import retrofit2.http.GET;
import retrofit2.http.POST;
import retrofit2.http.Part;

public interface ApiBanHang {
    @GET("getloaisp.php")
    Observable<LoaiSpModel> getLoaiSp();


    @GET("getDataSanPham.php")
    Observable<SanPhamMoiModel> getSpMoi();

    @POST("getDataDienThoai.php")
    @FormUrlEncoded
    Observable<SanPhamMoiModel> getSanPham(
            @Field("page") int page,
            @Field("loai") int loai
    );
}
