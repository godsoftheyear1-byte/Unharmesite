@echo off
echo ========================================
echo   DEPLOYING TO VERCEL
echo ========================================
echo.
echo This will open your browser to login to Vercel.
echo After logging in, it will automatically deploy!
echo.
pause
echo.
echo Starting deployment...
echo.
vercel --prod
echo.
echo ========================================
echo   DEPLOYMENT COMPLETE!
echo ========================================
echo.
echo Your site is now live!
echo Copy the URL shown above and share it!
echo.
pause
