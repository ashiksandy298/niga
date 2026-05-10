price = float(input("Enter the original price: "))
gst_rate = float(input("Enter GST rate (%): "))
total_gst = (price * gst_rate) / 100
cgst = total_gst / 2
sgst = total_gst / 2
final_price = price + total_gst
print("CGST:", round(cgst, 2))
print("SGST:", round(sgst, 2))
print("Total GST:", round(total_gst, 2))
print("Final Price (Including GST):", round(final_price, 2))
