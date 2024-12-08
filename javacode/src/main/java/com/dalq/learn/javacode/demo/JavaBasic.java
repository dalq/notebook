package com.dalq.learn.javacode.demo;

import org.apache.poi.xssf.usermodel.XSSFSheet;
import org.apache.poi.xssf.usermodel.XSSFWorkbook;

import java.io.File;
import java.io.FileInputStream;
import java.util.ArrayList;
import java.util.Calendar;
import java.util.Date;
import java.util.List;

/**
 * @author daling.qdl
 * @date 2024/6/10 上午8:54
 */
public class JavaBasic {
    public static void main(String[] args) {
        var v = List.of(1,2, 3);
        System.out.println(v);

        double a = 0.03;
        double b = 0.01;
        System.out.println(a - b);

        System.out.println(addDate(-1));

        String filePath = "/Users/quandaling/Desktop/工业机械覆盖类目.xlsx";
        File excelFile = new File(filePath);
        try (FileInputStream fileInputStream = new FileInputStream(excelFile);
             XSSFWorkbook wb = new XSSFWorkbook(fileInputStream);) {
            List<List<Object>> rowList = new ArrayList<>();
            ArrayList<Object> colList;
            XSSFSheet sheet = wb.getSheetAt(0);
            System.out.println("excel sheet rows: " + sheet.getPhysicalNumberOfRows());
        } catch (Exception e) {
            
        }
    }
    
    private static Date addDate(int days) {
        Calendar someDate = Calendar.getInstance();
        someDate.setTime(new Date());
        someDate.add(Calendar.DAY_OF_YEAR, -days);
        return someDate.getTime();
    }
    
    
}
