from math import sqrt, tan, pi

def calculate_adjustment(W, H, D_m, d, target_pixels_per_degree=60):
    """
    根据屏幕参数和观看距离计算每度的像素数，并给出具体的调整距离建议。
    
    W: 屏幕宽度，像素
    H: 屏幕高度，像素
    D_m: 屏幕对角线尺寸，米
    d: 当前观看距离，米
    target_pixels_per_degree: 目标每度像素数，默认为60
    """
    # 计算PPI
    D_inch = D_m / 0.0254  # 米转英寸
    PPI = sqrt(W**2 + H**2) / D_inch
    
    # 计算PPM（每米像素数）
    PPM = PPI / 0.0254
    
    # 计算当前每度的像素数
    current_pixels_per_degree = PPM * d * tan(1 * pi / 180)
    
    # 计算达到目标像素数的理想观看距离
    ideal_d = target_pixels_per_degree / (PPM * tan(1 * pi / 180))
    
    # 计算需要调整的距离
    adjustment = ideal_d - d
    
    if current_pixels_per_degree < target_pixels_per_degree:
        advice = f"为了达到目标每度像素数，建议增大观看距离，增加约{abs(adjustment):.2f}米。"
    elif current_pixels_per_degree > target_pixels_per_degree:
        advice = f"为了达到目标每度像素数，如果需要，可以减小观看距离，减少约{abs(adjustment):.2f}米。"
    else:
        advice = "当前距离提供了理想的视觉体验。"

    return current_pixels_per_degree, advice


# 用户输入
W = int(input("请输入屏幕宽度（像素）："))
H = int(input("请输入屏幕高度（像素）："))
D_m = float(input("请输入屏幕对角线尺寸（米）："))
d = float(input("请输入观看距离（米）："))

# 计算每度的像素数并获取建议
pixels_per_degree_example, advice_example = calculate_adjustment(W, H, D_m, d)
print(f"每度的像素数: {pixels_per_degree_example:.2f}")
print(advice_example)
