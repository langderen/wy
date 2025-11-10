package com.example.voting_back.controller;

import org.springframework.beans.factory.annotation.Value;
import org.springframework.core.io.FileSystemResource;
import org.springframework.core.io.Resource;
import org.springframework.http.HttpHeaders;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.multipart.MultipartFile;

import java.io.File;
import java.io.IOException;

@RequestMapping("/image")
@RestController
public class ImageUploadController {

    @Value("${upload.path}")
    private String uploadPath;

    @PostMapping("/upload")
    public String uploadImage(@RequestParam("file") MultipartFile file) {
        try {
            // 获取文件名
            String fileName = file.getOriginalFilename();
            // 指定保存路径
            String filePath = uploadPath + "/" + fileName;
            // 保存文件到本地
            file.transferTo(new File(filePath));
            return "上传成功";
        } catch (IOException e) {
            e.printStackTrace();
            return "上传失败";
        }
    }


    @GetMapping("/download")
    public ResponseEntity<Resource> downloadImage(@RequestParam("filename") String filename) {
        // 1. 构建文件路径（使用 File.separator 适配不同系统）
        File file = new File(uploadPath + File.separator + filename);

        // 2. 检查文件是否存在
        if (!file.exists() || !file.isFile()) {
            // 文件不存在时返回 404
            return new ResponseEntity<>(HttpStatus.NOT_FOUND);
        }

        // 3. 包装文件为 Spring 资源对象
        Resource resource = new FileSystemResource(file);

        // 4. 设置响应头：告知浏览器以附件形式下载，并处理中文文件名
        String encodedFilename;
        try {
            // 对文件名进行 UTF-8 编码，避免中文乱码
            encodedFilename = java.net.URLEncoder.encode(filename, "UTF-8");
        } catch (java.io.UnsupportedEncodingException e) {
            encodedFilename = filename; // 编码失败时使用原文件名
        }

        HttpHeaders headers = new HttpHeaders();
        // 设置 Content-Disposition 头，触发下载
        headers.add(HttpHeaders.CONTENT_DISPOSITION,
                "attachment; filename*=UTF-8''" + encodedFilename);

        // 5. 返回响应实体
        return new ResponseEntity<>(resource, headers, HttpStatus.OK);
    }
}
