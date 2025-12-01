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
  %6 = getelementptr inbounds [2 x i8], [2 x i8]* @.str2, i32 0, i32 0
  call i32 (i8*, ...) @scanf(i8* %6, i32* %0)
  %7 = getelementptr inbounds [23 x i8], [23 x i8]* @.str3, i32 0, i32 0
  %8 = getelementptr inbounds [3 x i8], [3 x i8]* @.str1, i32 0, i32 0
  call i32 (i8*, ...) @printf(i8* %8, i8* %7)
  %9 = getelementptr inbounds [2 x i8], [2 x i8]* @.str2, i32 0, i32 0
  call i32 (i8*, ...) @scanf(i8* %9, i32* %1)
  %10 = load i32, i32* %0
  %11 = load i32, i32* %1
  %12 = add i32 %10, %11
  %13 = fdiv double %12, 2.0
  store double %13, double* %2
  %14 = load double, double* %2
  %15 = fcmp oge double %14, 7.0
  br i1 %15, label %label0, label %label1
label0:
  %16 = getelementptr inbounds [17 x i8], [17 x i8]* @.str4, i32 0, i32 0
  %17 = getelementptr inbounds [3 x i8], [3 x i8]* @.str1, i32 0, i32 0
  call i32 (i8*, ...) @printf(i8* %17, i8* %16)
  %18 = load double, double* %2
  %19 = getelementptr inbounds [3 x i8], [3 x i8]* @.str5, i32 0, i32 0
  call i32 (i8*, ...) @printf(i8* %19, i32 %18)
  br label %label2
label1:
  %20 = getelementptr inbounds [18 x i8], [18 x i8]* @.str6, i32 0, i32 0
  %21 = getelementptr inbounds [3 x i8], [3 x i8]* @.str1, i32 0, i32 0
  call i32 (i8*, ...) @printf(i8* %21, i8* %20)
  %22 = load double, double* %2
  %23 = getelementptr inbounds [3 x i8], [3 x i8]* @.str5, i32 0, i32 0
  call i32 (i8*, ...) @printf(i8* %23, i32 %22)
  br label %label2
label2:
  store i32 1, i32* %3
  br label %label3
label3:
  %24 = load i32, i32* %3
  %25 = icmp sle i32 %24, 5
  br i1 %25, label %label4, label %label5
label4:
  %26 = getelementptr inbounds [10 x i8], [10 x i8]* @.str7, i32 0, i32 0
  %27 = getelementptr inbounds [3 x i8], [3 x i8]* @.str1, i32 0, i32 0
  call i32 (i8*, ...) @printf(i8* %27, i8* %26)
  %28 = load i32, i32* %3
  %29 = getelementptr inbounds [3 x i8], [3 x i8]* @.str5, i32 0, i32 0
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
@.str2 = private unnamed_addr constant [3 x i8] c"%d\00"
@.str3 = private unnamed_addr constant [23 x i8] c"Digite a segunda nota:\00"
@.str4 = private unnamed_addr constant [17 x i8] c"Aprovado! Média:\00"
@.str5 = private unnamed_addr constant [6 x i8] c"%d\5C0A\00"
@.str6 = private unnamed_addr constant [18 x i8] c"Reprovado. Média:\00"
@.str7 = private unnamed_addr constant [10 x i8] c"Contador:\00"