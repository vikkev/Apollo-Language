; Código LLVM IR gerado para Apollo

declare i32 @printf(i8*, ...)
declare i32 @scanf(i8*, ...)

define i32 @main() {
entry:
  %0 = alloca i32
  store i32 0, i32* %0
  %1 = alloca i32
  store i32 0, i32* %1
  %2 = alloca double
  store double 0.0, double* %2
  %3 = alloca i32
  store i32 0, i32* %3
  %4 = getelementptr inbounds [24 x i8], [24 x i8]* @.str0, i32 0, i32 0
  %5 = getelementptr inbounds [3 x i8], [3 x i8]* @.str1, i32 0, i32 0
  call i32 (i8*, ...) @printf(i8* %5, i8* %4)
  store i32 0, i32* %0
  %6 = getelementptr inbounds [23 x i8], [23 x i8]* @.str2, i32 0, i32 0
  %7 = getelementptr inbounds [3 x i8], [3 x i8]* @.str1, i32 0, i32 0
  call i32 (i8*, ...) @printf(i8* %7, i8* %6)
  store i32 0, i32* %1
  %8 = load i32, i32* %0
  %9 = load i32, i32* %1
  %10 = add i32 %8, %9
  %11 = sdiv i32 %10, 2.0
  store i32 %11, i32* %2
  %12 = load i32, i32* %2
  %14 = icmp sge i32 %12, 7.0
  %13 = zext i1 %14 to i32
  br i1 %13, label %label0, label %label1
label0:
  %15 = getelementptr inbounds [17 x i8], [17 x i8]* @.str3, i32 0, i32 0
  %16 = getelementptr inbounds [3 x i8], [3 x i8]* @.str1, i32 0, i32 0
  call i32 (i8*, ...) @printf(i8* %16, i8* %15)
  %17 = load i32, i32* %2
  %18 = getelementptr inbounds [3 x i8], [3 x i8]* @.str4, i32 0, i32 0
  call i32 (i8*, ...) @printf(i8* %18, i32 %17)
  br label %label2
label1:
  %19 = getelementptr inbounds [18 x i8], [18 x i8]* @.str5, i32 0, i32 0
  %20 = getelementptr inbounds [3 x i8], [3 x i8]* @.str1, i32 0, i32 0
  call i32 (i8*, ...) @printf(i8* %20, i8* %19)
  %21 = load i32, i32* %2
  %22 = getelementptr inbounds [3 x i8], [3 x i8]* @.str4, i32 0, i32 0
  call i32 (i8*, ...) @printf(i8* %22, i32 %21)
  br label %label2
label2:
  store i32 1, i32* %3
  br label %label3
label3:
  %23 = load i32, i32* %3
  %25 = icmp sle i32 %23, 5
  %24 = zext i1 %25 to i32
  br i1 %24, label %label4, label %label5
label4:
  %26 = getelementptr inbounds [10 x i8], [10 x i8]* @.str6, i32 0, i32 0
  %27 = getelementptr inbounds [3 x i8], [3 x i8]* @.str1, i32 0, i32 0
  call i32 (i8*, ...) @printf(i8* %27, i8* %26)
  %28 = load i32, i32* %3
  %29 = getelementptr inbounds [3 x i8], [3 x i8]* @.str4, i32 0, i32 0
  call i32 (i8*, ...) @printf(i8* %29, i32 %28)
  br label %label3
label5:
  %30 = load i32, i32* %3
  %31 = add i32 %30, 1
  store i32 %31, i32* %3
  ret i32 0
}

@.str0 = private unnamed_addr constant [24 x i8] c"Digite a primeira nota:\00"
@.str1 = private unnamed_addr constant [6 x i8] c"%s\5C0A\00"
@.str2 = private unnamed_addr constant [23 x i8] c"Digite a segunda nota:\00"
@.str3 = private unnamed_addr constant [17 x i8] c"Aprovado! Média:\00"
@.str4 = private unnamed_addr constant [6 x i8] c"%d\5C0A\00"
@.str5 = private unnamed_addr constant [18 x i8] c"Reprovado. Média:\00"
@.str6 = private unnamed_addr constant [10 x i8] c"Contador:\00"